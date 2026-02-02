document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', () => compose_email());

  // Send the eamil
  document.querySelector('#compose-form').addEventListener('submit', send_mail)
  // By default, load the inbox
  load_mailbox('inbox');
});

const VIEW_IDS = ['emails-view', 'email-view', 'compose-view'];


// a helper function to show one view and hide the others

function showView(viewId) {
  for (const view of VIEW_IDS) {
    document.getElementById(view).style.display = (view === viewId) ? 'block' : 'none';
  }
}


// a helper function to make API requests

async function apiRequest(path, { method = 'GET', body = null } = {}) {
  const options = { method };
  if (body !== null) {
    options.headers = { 'Content-Type': 'application/json' };
    options.body = JSON.stringify(body);
  }

  const response = await(fetch(path, options));

  const body_text = await response.text();
  const data = body_text ? JSON.parse(body_text) : null;

  if (!response.ok) {
    throw new Error(data?.error ?? `Request failed! HTTP ${response.status}: ${response.statusText}`);
  }

  return data;
}


// small wrappers for different API endpoints

const apiGetMailbox = (mailbox) => apiRequest(`/emails/${mailbox}`);

const apiGetEmail = (id) => apiRequest(`/emails/${id}`);

const apiSendEmail = (recipients, subject, body) => apiRequest('/emails', {
  method: 'POST',
  body: { recipients, subject, body }
});

const apiUpdateEmail = (id, patch) => apiRequest(`/emails/${id}`, {
  method: 'PUT',
  body: patch
});



function compose_email(prefill = {}) {
  showView('compose-view');

  const recipientsField = document.querySelector('#compose-recipients');
  const subjectField = document.querySelector('#compose-subject');
  const bodyField = document.querySelector('#compose-body');

  recipientsField.value = prefill.recipients ?? '';
  subjectField.value = prefill.subject ?? '';
  bodyField.value = prefill.body ?? '';
}


async function send_mail(event) {
  event.preventDefault();

  const receptiants = document.querySelector('#compose-recipients').value.trim();
  const subject = document.querySelector('#compose-subject').value.trim();
  const body = document.querySelector('#compose-body').value;

  try {
    await apiSendEmail(receptiants, subject, body);
    load_mailbox('sent');
  }
  catch(error) {
    alert(error.message)
  }
}



async function load_mailbox(mailbox) {
  showView('emails-view');
 
  const view = document.querySelector('#emails-view');
  view.replaceChildren();
  
  const title = document.createElement('h3');
  title.textContent = `${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}`;
  view.appendChild(title);

  try {
    const emails = await apiGetMailbox(mailbox);

    if (!emails.length) {
      const empty_paragraph = document.createElement('p');
      empty_paragraph.textContent = 'No emails here.';
      view.appendChild(empty_paragraph);
      return;
    }

    const list = document.createElement('ul');
    list.classList.add('email-list');
    view.appendChild(list);

    emails.forEach(email => {
      const row = buildEmailRow(email, mailbox);
      list.appendChild(row)
    });
}
  catch(error) {
    const error_paragraph = document.createElement('p');
    error_paragraph.textContent = `Error: ${error.message}`;
    view.replaceChildren(error_paragraph);
  }
}


function buildEmailRow(email, mailbox) {
  const item = document.createElement('li');
  item.classList.add('email-item');

  const button = document.createElement('button');
  button.type = 'button';
  button.classList.add('email-row');
  button.classList.add(email.read ? 'read' : 'unread');

  const fromTo = document.createElement('div');
  fromTo.classList.add('email-fromto');
  const fromToLabel = document.createElement('strong');
  fromToLabel.textContent = (mailbox === 'sent') ? 'To:' : 'From:';
  const fromToValue = (mailbox === 'sent') ? email.recipients.join(', ') : email.sender;
  fromTo.append(fromToLabel, document.createTextNode(` ${fromToValue}`));
  button.appendChild(fromTo);

  const subject = document.createElement('div');
  subject.classList.add('email-subject');
  subject.textContent = `${email.subject}`;
  button.appendChild(subject);

  const timestamp = document.createElement('time');
  timestamp.classList.add('email-timestamp');
  timestamp.textContent = email.timestamp;
  button.appendChild(timestamp);

  button.addEventListener('click', async () => {
    const opened = await openEmail(email.id, mailbox);
    if (opened) {
      button.classList.remove('unread');
      button.classList.add('read');
    }
  });

  item.appendChild(button);
  return item;

}


async function openEmail(id, mailbox) {
  showView('email-view');

  const view = document.querySelector('#email-view');
  view.replaceChildren();

  let email;
  try {
    email = await apiGetEmail(id);
  }
  catch(error) {
    const error_paragraph = document.createElement('p');
    error_paragraph.textContent = `Error: ${error.message}`;
    view.replaceChildren(error_paragraph);
    return false;
  }

  view.appendChild(createEmailContent(email, mailbox));

  if (mailbox !== 'sent') {
    const toggleArchiveButton = view.querySelector('.toggle-archive');
    toggleArchiveButton?.addEventListener('click', async () => {
      toggleArchiveButton.disabled = true;
      try {
        await apiUpdateEmail(id, { archived: !email.archived });
        load_mailbox('inbox');
      }
      catch(error) {
        toggleArchiveButton.disabled = false;
        console.log(error.message);
      }
    });

    const replyButton = view.querySelector('.reply-button');
    replyButton?.addEventListener('click', () => replyFill(email));
  }

  if (!email.read) {
    apiUpdateEmail(id, { read: true }).catch(error => console.log(error.message));
  }

  return true;
}


function createEmailContent(email, mailbox) {
  const container = document.createElement('div');
  container.classList.add('email-detail');
  const header = document.createElement('div');
  header.classList.add('email-detail-header');
  const body = document.createElement('div');
  body.classList.add('email-detail-body');
  const actions = document.createElement('div');
  actions.classList.add('email-detail-actions');

  const sender = document.createElement('p');
  sender.classList.add('email-sender');
  const senderLabel = document.createElement('strong');
  senderLabel.textContent = 'From:';
  sender.append(senderLabel, document.createTextNode(` ${email.sender}`));
  header.appendChild(sender);

  const recipients = document.createElement('p');
  recipients.classList.add('email-recipients');
  const recipientsLabel = document.createElement('strong');
  recipientsLabel.textContent = 'To:';
  recipients.append(recipientsLabel, document.createTextNode(` ${email.recipients.join(', ')}`));
  header.appendChild(recipients);

  const timestamp = document.createElement('time');
  timestamp.classList.add('email-timestamp');
  const timestampLabel = document.createElement('strong');
  timestampLabel.textContent = 'Sent at:';
  timestamp.append(timestampLabel, document.createTextNode(` ${email.timestamp}`));
  header.appendChild(timestamp);

  const subject = document.createElement('p');
  subject.classList.add('email-subject');
  const subjectLabel = document.createElement('strong');
  subjectLabel.textContent = 'Subject:';
  subject.append(subjectLabel, document.createTextNode(` ${email.subject}`));
  header.appendChild(subject);

  const body_text = document.createElement('pre');
  body_text.classList.add('email-body');
  body_text.textContent = `${email.body}`;
  body.appendChild(body_text);

  if (mailbox !== 'sent') {
    const toggleArchiveButton = document.createElement('button');
    toggleArchiveButton.type = 'button';
    toggleArchiveButton.classList.add('toggle-archive', 'btn', 'btn-sm', 'btn-outline-secondary');
    toggleArchiveButton.textContent = email.archived ? 'Unarchive' : 'Archive';
    actions.appendChild(toggleArchiveButton);
  }


  const replyButton = document.createElement('button');
  replyButton.type = 'button';
  replyButton.classList.add('reply-button', 'btn', 'btn-sm', 'btn-outline-primary');
  replyButton.textContent = 'Reply';
  actions.appendChild(replyButton);
  

  container.appendChild(header);
  container.appendChild(body);
  container.appendChild(actions);

  return container;
}

function replyFill(email) {
    const recipients = email.sender;

    const subject = (email.subject.toLowerCase().startsWith('re: ')) ? email.subject : `Re: ${email.subject}`;
    
    const body = `\n\nOn ${email.timestamp} ${email.sender} wrote:\n${email.body}\n`;
    
    compose_email({ recipients, subject, body });

    const bodyField = document.querySelector('#compose-body');
    bodyField.focus();
    bodyField.setSelectionRange(0, 0);
}
