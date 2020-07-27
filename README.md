# GNU Stow Plugin for Dotbot

Link dotfiles with Stow.

# Installation

Add this repo as a submodule to your dotfiles repo:

`git submodule add https://github.com/timbedard/dotbot-stow`

Modify your `install` script:

```bash
"${BASEDIR}/${DOTBOT_DIR}/${DOTBOT_BIN}" -d "${BASEDIR}" --plugin-dir dotbot-stow -c "${CONFIG}" "${@}"
```

# Usage

```yaml
# simple
- stow: scripts

# list
- stow: ['bin', 'utils']

# dict
- stow:
    nvim: ~/.config/nvim

# full config
- stow:
    config:
      target: ~/.config
      restow: true
      adopt: false
      ignore: "md"
      defer: "flake8"
      override: "fish"
    vim:
```
