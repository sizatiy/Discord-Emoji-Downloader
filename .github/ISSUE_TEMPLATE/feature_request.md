name: Feature Request
description: Suggest an improvement
title: "[FEATURE] "
labels: ["enhancement"]

body:
  - type: textarea
    id: description
    attributes:
      label: Describe the feature
      description: Clear description of what you want to add
    validations:
      required: true

  - type: textarea
    id: solution
    attributes:
      label: Suggested solution
      description: How should this feature work?
    validations:
      required: false

  - type: textarea
    id: alternatives
    attributes:
      label: Alternative solutions
      description: Other ways to solve this?
    validations:
      required: false
