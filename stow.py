import subprocess

from dotbot import Plugin


class Stow(Plugin):
    _directive = "stow"

    def can_handle(self, directive):
        return directive == self._directive

    def handle(self, directive, data):
        if directive != self._directive:
            raise ValueError("Stow cannot handle directive %s" % directive)
        return self._process(data)

    def _process(self, packages):
        success = True
        defaults = self._context.defaults().get("stow", {})
        if isinstance(packages, str):
            options = defaults.copy()
            options["package"] = packages
            self._stow(**options)
        elif isinstance(packages, list):
            for package in packages:
                options = defaults.copy()
                options["package"] = package
                self._stow(**options)
        elif isinstance(packages, dict):
            for package, value in packages.items():
                options = defaults.copy()
                if isinstance(value, dict):
                    options["package"] = package
                    options.update(value)
                else:
                    options.update(
                        {"package": package, "target": value,}
                    )
                self._stow(**options)
        return success

    def _stow(self, package=".", target=None, restow=True, adopt=False, **kwargs):
        options = [
            "--dir={}".format(self._context.base_directory()),
            "--target={}".format(target) if target else None,
            "--restow" if restow else "--stow",
            "--adopt" if adopt else None,
        ]

        for ptn_option in (o for o in ("ignore", "defer", "override") if o in kwargs):
            ptns = kwargs.get(ptn_option)
            if not isinstance(ptns, list):
                ptns = [ptns]
            for ptn in ptns:
                options.append("--{}={}".format(ptn_option, ptn))

        cmd = ["stow"] + [o for o in options if o] + [package]
        subprocess.check_output(cmd)
