####################################################
# OUR PROGRAM
####################################################

import views,models
from models import app

if __name__ == '__main__':
    app.debug=True
    app.run()
