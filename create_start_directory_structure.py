# create_start_directory_structure.py
import os

def create_structure(base_dir):
    # Define the directories and files structure
    structure = {
        'app': {
            'Http': {
                'Controllers': {
                    'API': {
                        'OrderApiController.php': None
                    },
                    'ManagerRegistrationController.php': None,
                    'OrderController.php': None,
                },
                'UserSettingController.php': None,
            },
            'User.php': None
        },
        'database': {
            'migrations': {
                'xxxx_xx_xx_create_orders_table.php': None,
                'xxxx_xx_xx_create_user_settings_table.php': None,
                'xxxx_xx_xx_create_users_table.php': None,
            },
            'seeds': {
                'DatabaseSeeder.php': None
            }
        },
        'resources': {
            'views': {
                'auth': {
                    'login.blade.php': None,
                    'register.blade.php': None,
                },
                'orders': {
                    'index.blade.php': None,
                    'show.blade.php': None,
                },
                'settings': {
                    'index.blade.php': None
                },
                'welcome.blade.php': None,
            }
        },
        'routes': {
            'api.php': None,
            'web.php': None
        },
        '.env': None,
        'composer.json': None,
        'package.json': None,
        'webpack.mix.js': None
    }
    
    def create_substructure(path, substructure):
        for key, value in substructure.items():
            new_path = os.path.join(path, key)
            if value is None:
                # It's a file
                open(new_path, 'w').close()
            else:
                # It's a directory
                os.makedirs(new_path, exist_ok=True)
                create_substructure(new_path, value)
    
    create_substructure(base_dir, structure)

base_directory = "OrderPanel"
os.makedirs(base_directory, exist_ok=True)
create_structure(base_directory)
