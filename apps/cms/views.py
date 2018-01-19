from flask import Blueprint,views,render_template,request,session,redirect,url_for,g
from .form import LoginForm,ResetpwdForm
from .models import CMSUser
from .decorator import login_required
from config import CMS_USER_ID
bp = Blueprint('cms',__name__,url_prefix='/cms')

@bp.route('/')
@login_required
def index():
    return render_template('cms/cms_index.html')

@bp.route('/logout')
@login_required
def logout():
    session.clear()
    'del session[config.CMS_USER_ID'
    return redirect(url_for('cms.login'))

@bp.route('/profile')
@login_required
def profile():
    return render_template('cms/cms_profile.html')


class LoginView(views.MethodView):

    def get(self,message=None):
        return render_template('cms/cms_login.html',message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[CMS_USER_ID] = user.id
                if remember:

                    session.permanent = True
                else:
                    session.permanent = False
                    print ('cool')
                return redirect(url_for('cms.index'))
            else:
                print('not cool')
                return self.get(message='email or password incorrect')

        else:
            print('papapa cool')
            message = form.errors.popitem()[1][0]
            print(message)
            return self.get(message=message)

class ResetPwdView(views.MethodView):
    decorators = [login_required]
    def get(self):
        return render_template('cms/cms_resetpwd.html')

    def post(self):
        form = ResetpwdForm(request.form)
        if form.validate():
            pass




bp.add_url_rule('/login/',view_func=LoginView.as_view('login'))
bp.add_url_rule('/resetpwd/',view_func=ResetPwdView.as_view('resetpwd'))