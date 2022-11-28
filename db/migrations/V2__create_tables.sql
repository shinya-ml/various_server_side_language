create table if not exists users (
   id integer generated always as identity,
   name varchar not null default '',
   age integer not null default 0,
   created_at timestamptz not null default now(),
   primary key (id)
);

create table if not exists todos (
    id integer generated always as identity,
    title varchar not null default '',
    memo text not null default '',
    primary key (id)
);