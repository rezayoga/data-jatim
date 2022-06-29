from app import create_app

application = create_app('config.DevelopmentConfig')

if __name__ == '__main__':
  application.run(debug=True)
