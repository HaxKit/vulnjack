# VulnJack

VulnJack is a command-line tool that scrapes a given website and checks for the presence of the `Strict-Transport-Security` header in the URLs found on the site. It helps identify if the security header is missing or present, improving the security posture of websites.

## Features

- Scrapes URLs from a specified website.
- Checks if the `Strict-Transport-Security` header is present for each URL.
- Outputs the result for each URL, indicating whether the header is missing or present.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ HaxKit/vulnjack.git
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run VulnJack, use the following command:

```bash
vulnjack --url <website_url>
```

### Example

```bash
vulnjack.py --url https://example.com
```

This will scrape all the URLs from `https://example.com` and check for the presence of the `Strict-Transport-Security` header.

## Requirements

- Python 3.x
- `scraply` library (for scraping URLs)
- `vulheader` library (for header checking)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
