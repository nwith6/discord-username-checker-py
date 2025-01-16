# Discord Username Checker
This is a basic username checking tool. This project can generate usernames, or just check a specific username.

You can configure information regarding the generation of usernames, the length of usernames, and the time between usernames checks.


## How does this work?
Based on a regular expression this application will generate a string that is then checked for its availability on discord. Opening the `config.json` file will show you a few easy to understand options. Tinker around with and configure these options to your liking.

### Example Regex
- `[0-9]{3}` - 3 digit string, ranging between numbers "0" and "9".
- `[a-z]{7}` - 7 letter string ranging between letters "a" and "z".
- `[0-9a-z]{10}` - 10 character string.
- `[0-9a-z_.]{15}` - 15 character string including "." and "_".
- `[0-9a-z_.]{3,5}` - 3-5 character string including "." and "_".
- `specific_username123` - Ignores generation and will chech specifically for "specified_username123".
- `12[a-z]{3}` - Prefixes a 3 letter generated string with "12"
- `9[2-5]{1}[a-f]{3,7}` - Prefixes a singular generated number that is between 2 and 5 with 9 and appends a generated 3-7 character string that consists of letters between "a" and "f".

## If you need to contact me
You can add me on discord @hiwv
