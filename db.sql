create Table Todo (
  id INTEGER primary key  AUTOINCREMENT,
  todo varchar(30) not null,
  done BOOLEAN DEFAULT(0)
)
