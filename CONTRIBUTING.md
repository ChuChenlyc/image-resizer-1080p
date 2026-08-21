# Contributing to Image Resizer 1080P

Thank you for your interest in contributing! This document explains how to report issues, request features, and submit changes.

## Reporting Bugs

Please open an issue on the [Issues page](https://github.com/chuchenlyc/image-resizer-1080p/issues) and include:

- Your operating system and Python version (if running from source)
- Steps to reproduce the problem
- The image format(s) involved (PNG, JPEG, BMP, GIF, WebP)
- Any error messages shown in the status bar or console

## Requesting Features

Feature ideas are welcome on the [Discussions page](https://github.com/chuchenlyc/image-resizer-1080p/discussions). Please describe the use case so the benefit is clear.

## Development Setup

1. Ensure Python 3.6+ is installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/chuchenlyc/image-resizer-1080p.git
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python src/main.py
   ```

## Submitting Pull Requests

- Keep changes small and focused on a single fix or feature.
- Test the GUI manually on Windows before submitting: select an input folder, run a conversion, and verify the 1920x1080 output with transparent padding.
- Describe what you changed and why in the pull request body.
- Note that converted output files are always saved as PNG; changes affecting format handling should be called out explicitly.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
