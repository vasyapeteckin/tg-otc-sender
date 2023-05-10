

# Telegram OTC Sender

This is a project that allows sending to OTC chats on Telegram using Pyrogram.

## Installation

1. Clone this repository or download the code as a ZIP file and extract it.
2. Install the required packages using pip:
```
pip install -r requirements.txt
```
3. Rename the file `example.env` to `.env` and fill in the required information. Instructions for this step can be found below.

## Configuration



The `.env` file is used to store sensitive information such as API credentials and configuration options. This file should never be committed to version control and should be kept secret.

The options that can be set in the `.env` file for this project are:

- `api_id` and `api_hash`: Your Telegram API credentials. You can get them by creating a new application on the [Telegram website](https://my.telegram.org/apps).
- `path_to_otc_chats`: The path to the file that contains a list of chat IDs that will receive the OTC trades. This file should contain one chat ID per line.
- `path_to_message_text`: The path to the file that contains text message.

An example `.env` file might look like this:

```
api_id=123456
api_hash=abcdef1234567890abcdef1234567890
path_to_otc_chats=/path/to/chats.txt
path_to_message_text=/path/to/message/text.txt
```

## Usage

To start the OTC trade, simply run the `sender.py` script:

```
python sender.py
```

The script will ask you to confirm the trade details before sending the trade to the receiver.

## Contributing

This project is open to contributions. If you find a bug or have a suggestion for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.