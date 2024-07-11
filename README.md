# l33tpass.py


This script generates leetspeak passwords from a list of usernames. It provides several command-line options to customize the generated passwords, including capitalization, appending/prepending strings, and customizing the leetspeak dictionary.

## Default Leetspeak Dictionary

```python
{
    'a': '@', 'b': '8', 'e': '3', 'g': '6', 'i': '1', 'l': '1',
    'o': '0', 's': '5', 't': '7', 'z': '2', 'A': '4', 'B': '8',
    'E': '3', 'G': '6', 'I': '1', 'L': '1', 'O': '0', 'S': '5',
    'T': '7', 'Z': '2'
}
```

## Usage

```sh
python3 l33tpass.py <input_file> [options]
```

### Required Arguments

- `input_file`: File containing usernames, one per line.

### Optional Arguments

- `-o`, `--output_file`: Output file to write the username:password pairs. If not provided, output is printed to the console.
- `-c`, `--capitalize`: Capitalize the first letter of the password.
- `-a`, `--append`: String to append to the end of each password.
- `-p`, `--prepend`: String to prepend to the beginning of each password.
- `-s`, `--separator`: Separator to use between username and password (default is `:`).
- `-i`, `--include`: List of keys to include in the leetspeak replacements. Only the instances of the characters on the list provided will be replaced by the associated leet value in the output passwords.
- `-e`, `--exclude`: List of keys to exclude from the leetspeak replacements. All characters except those listed will be replaced by the leet value.
- `-u`, `--custom`: List of custom key:value pairs to modify the leetspeak dictionary.

### Examples

1. Basic usage with default settings:
    ```sh
    python3 l33tpass.py usernames.txt
    ```

2. Capitalize the first letter of each password:
    ```sh
    python3 l33tpass.py usernames.txt -c
    ```

3. Append a string to the end of each password:
    ```sh
    python3 l33tpass.py usernames.txt -a "123"
    ```

4. Prepend a string to the beginning of each password:
    ```sh
    python3 l33tpass.py usernames.txt -p "!"
    ```

5. Use a space separator instead of a colon:
    ```sh
    python3 l33tpass.py usernames.txt -s " "
    ```

6. Include only certain characters for leetspeak replacement:
    ```sh
    python3 l33tpass.py usernames.txt -i a e o
    ```

7. Exclude certain characters from leetspeak replacement:
    ```sh
    python3 l33tpass.py usernames.txt -e i l
    ```

8. Customize the leetspeak dictionary:
    ```sh
    python3 l33tpass.py usernames.txt -u a:@ o:0
    ```


