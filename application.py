import sys
from api import create_app

application = create_app()


def main():
    application.run(reloader=False, debug=None)
    
    
def before_main():
    args = sys.argv[1:]
    
    if args[0] == "run_migration":
        from manual_migrations.run_migrations import run
        run()
    
    
if __name__ == "__main__":
    before_main()
    main()
    