 CREATE TABLE `personal`
  (
    `user_id` Uint64,
    `chat_id` Uint64,
    `username` Utf8,
    `registration_date` Datetime,
    PRIMARY KEY (`user_id`)
  );

  COMMIT;

  CREATE TABLE `states`
  (
    `user_id` Uint64,
    `state` Utf8,
    PRIMARY KEY (`user_id`)
  );