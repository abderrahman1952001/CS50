SELECT name FROM schools
wHERE id IN
(SELECT school_id FROM graduation_rates
      WHERE graduated = '100');

