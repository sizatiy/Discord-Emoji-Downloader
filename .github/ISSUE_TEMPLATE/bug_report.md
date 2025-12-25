name: Bug Report
description: Report a bug with the Discord Emoji Downloader
title: "[BUG] "
labels: ["bug"]

body:
  - type: textarea
    id: description
    attributes:
      label: Describe the bug
      description: A clear description of what the bug is
    validations:
      required: true

  - type: textarea
    id: steps
    attributes:
      label: Steps to reproduce
      description: Steps to reproduce the behavior
      placeholder: |
        1. Go to...
        2. Click...
        3. See error...
    validations:
      required: true

  - type: textarea
    id: expected
    attributes:
      label: Expected behavior
      description: What should happen instead?
    validations:
      required: true

  - type: textarea
    id: error
    attributes:
      label: Error message or screenshot
      description: Paste any error messages or screenshots
    validations:
      required: false

  - type: dropdown
    id: platform
    attributes:
      label: Platform
      options:
        - Windows (.EXE)
        - Windows (Python)
        - Other
    validations:
      required: true
