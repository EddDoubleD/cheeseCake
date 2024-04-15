PERSONAL_INFO_TABLE_PATH = "personal"
STATES_TABLE_PATH = "states"

get_user_state = f"""
    DECLARE $user_id AS Uint64;

    SELECT state
    FROM `{STATES_TABLE_PATH}`
    WHERE user_id == $user_id;
"""

set_user_state = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $state AS Utf8?;

    UPSERT INTO `{STATES_TABLE_PATH}` (`user_id`, `state`)
    VALUES ($user_id, $state);
"""

delete_state = f"""
    DECLARE $user_id AS Uint64;
    
    DELETE FROM `{STATES_TABLE_PATH}`
    WHERE user_id == $user_id;
"""

save_primary_personal_info = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $chat_id AS Uint64;
    DECLARE $username AS Utf8;
    $now = CurrentUtcDatetime();

    INSERT INTO `{PERSONAL_INFO_TABLE_PATH}` (`user_id`, `chat_id`, `username`, `registration_date`) 
    VALUES ($user_id, $chat_id, $username, $now);
"""

delete_user_info = f"""
    DECLARE $user_id AS Uint64;

    DELETE FROM `{PERSONAL_INFO_TABLE_PATH}`
    WHERE user_id == $user_id;

    DELETE FROM `{STATES_TABLE_PATH}`
    WHERE user_id == $user_id;
"""

get_user_info = f"""
    DECLARE $user_id AS Int64;

    SELECT
        user_id,
        chat_id,
        username,
    FROM `{PERSONAL_INFO_TABLE_PATH}`
    WHERE user_id == $user_id;
"""
