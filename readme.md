# Discord Username Checker
This is a basic username checking tool. This project can generate usernames, or just check a specific username.

You can configure information regarding the generation of usernames, the length of usernames, and the time between usernames checks.


## How does this work?
Based on a regular expression this application will generate a string that is then checked for its availability on discord. Opening the `config.json` file will show you a few easy to understand options. Tinker around with and configure these options to your liking.

### Example Regex
- `[0-9]{3}` - 3 digit string.
- `[a-z]{7}` - 7 letter string.
- `[0-9a-z]{10}` - 10 character string.
- `[0-9a-z_.]{15}` - 15 character string including "." and "_".

## If you need to contact me
You can add me on discord @hiwv
