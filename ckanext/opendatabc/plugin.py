import ckan.plugins as p
import ckan.plugins.toolkit as tk

class OpenDataBCTheme(p.SingletonPlugin):
    
    p.implements(p.IConfigurer)

    def update_config(self, config):

	tk.add_resource('fanstatic', 'opendatabc')
	tk.add_public_directory(config, 'public')
        tk.add_template_directory(config, 'templates')
 
