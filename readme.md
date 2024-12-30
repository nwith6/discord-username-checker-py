# Discord Username Checker
This is a basic username checking tool. This project can generate usernames, or just check a specific username.

You can configure information regarding the generation of usernames, the length of usernames, and the time between usernames checks.

## Modes
In `config.json` there is a `mode` property, the modes and their definition are:

1. `l`: If the mode has the character `l` it will use the defined letters (`letters`) in the config file.
2. `d`: If the mode has the character `d` it will use the defined letters (`digits`) in the config file.
3. `s`: If the mode has the character `s` it will use the defined letters (`specials`) in the config file.
4. `specific` If the mode is set to "specific" it will check for the specific username defined by the `username` property and not generate random usernames to check.

### How does this work?
You can chain these together so for example setting the `mode` to `"lds"` will generate usernames containing the defined `letters`, `digits`, and `specials`. If you were to only do `ld` it will generate usernames with the defined `letters` and `digits`, avoiding the the defined `specials`.

# If you need to contact me
You can add me on discord @hiwv
