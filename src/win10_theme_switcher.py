import keypirinha as kp
from .lib import regobj

class Win10ThemeSwitcher(kp.Plugin):
	"""Dark / Light Theme Toggle Switcher for Windows 10"""

	ITEMCAT_RESULT = kp.ItemCategory.USER_BASE + 1

	def __init__(self):
		super().__init__()

	def on_start(self):
		pass

	def on_catalog(self):
		self.merge_catalog([self.create_item(
			category=self.ITEMCAT_RESULT,
			label="Win 10 Themes Switcher: Toggle",
			short_desc="Toggle Windows 10 Theme: Light / Dark",
			target="win10themeswitcher:toggle",
			args_hint=kp.ItemArgsHint.FORBIDDEN,
			hit_hint=kp.ItemHitHint.NOARGS
		)])

	def on_suggest(self, user_input, items_chain):
		pass

	def on_execute(self, item, action):
		if item and item.category() == self.ITEMCAT_RESULT:
			try:
				theme = regobj.HKCU.Software.Microsoft.Windows.CurrentVersion.Themes.Personalize['AppsUseLightTheme'].data
				regobj.HKCU.Software.Microsoft.Windows.CurrentVersion.Themes.Personalize["AppsUseLightTheme"] = 1 if theme == 0 else 0
			except AttributeError:
				self.error("Win10ThemeSwitcher not found in registry.")
