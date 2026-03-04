def update_memo(old_memo, new_data):

    changes = []

    for key, value in new_data.items():

        if key not in old_memo or old_memo[key] != value:
            old_memo[key] = value
            changes.append(f"{key} updated")

    return old_memo, changes