CREATE TABLE IF NOT EXISTS thoth (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
name_orig text NOT NULL,
name_rus text NOT NULL,
suit text NOT NULL,
card_number integer NOT NULL,
description text NOT NULL,
description_rus NOT NULL
)