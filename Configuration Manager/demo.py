from user import add_setting, update_setting, delete_setting, view_settings

settings = {
    "theme": "light",
    "language": "english",
    "notifications": "enabled",
}

print(view_settings(settings))

print(add_setting(settings, ("volume", "high")))
print(add_setting(settings, ("theme", "dark")))  # already exists

print(update_setting(settings, ("theme", "dark")))
print(update_setting(settings, ("brightness", "low")))  # doesn't exist

print(delete_setting(settings, "language"))
print(delete_setting(settings, "language"))  # already deleted

print(view_settings(settings))
print(view_settings({}))  # empty settings
