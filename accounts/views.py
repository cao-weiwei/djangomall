from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.contrib import auth
from django.conf import settings
from .forms import LoginForm, SignupForm
from requests_oauthlib import OAuth1Session


def signup(request):
    # 使用 SignupForm，接受 POST 请求内容
    form = SignupForm(request.POST or None)
    # 如果表单验证成功，保存数据
    if form.is_valid():
        form.save()
        redirect_url = 'login'
        # 获取验证后的 Email 和密码
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        # 认证用户
        user = auth.authenticate(username=email, password=password)

        # 认证成功，登录
        if user:
            auth.login(request, user)
            redirect_url = settings.LOGIN_REDIRECT_URL

        return redirect(redirect_url)
    # 表单验证不成功（包括 GET 请求）显示注册模版
    ctx = {'form': form}
    return TemplateResponse(request, 'accounts/signup.html', ctx)


class LoginView(auth_views.LoginView):
    # 指定 accounts/login.html 作为模版
    template_name = 'accounts/login.html'
    # 表单改成 AuthenticationFormExample
    form_class = LoginForm



KEY = 'b5VPY9kYU94YvAMzefNY5RkdFGtwS2vc9XPiIepq'
SECRET = 'nafEASaKDkiAWisKHdF6VQr6gzkBUyURpLBGc3Xn'
BASE_URL = 'https://api06.dev.openstreetmap.org/'


def oauth_login(request):
    oauth = OAuth1Session(KEY, client_secret=SECRET)

    # 请求 token
    request_token_url = BASE_URL + 'oauth/request_token'
    fetch_response = oauth.fetch_request_token(request_token_url)
    # 得到返回的 token 和 token_secret，token 作为 url 参数，token_secret 保存到 session
    request.session['oauth_token_secret'] = fetch_response['oauth_token_secret']
    oauth_url = BASE_URL + 'oauth/authorize' + \
        '?oauth_token=' + fetch_response['oauth_token']
    return redirect(oauth_url)


def oauth_callback(request):
    oauth = OAuth1Session(KEY, client_secret=SECRET)
    # 获得完整 URL
    full_url = request.build_absolute_uri()
    # 从 URL 拿到 Token
    oauth_response = oauth.parse_authorization_response(full_url)

    # 再次调用 OAuth1Session，传递 Token 和之前的 Secret
    oauth = OAuth1Session(
        KEY,
        client_secret=SECRET,
        resource_owner_key=oauth_response['oauth_token'],
        resource_owner_secret=request.session['oauth_token_secret'],
        verifier=request.session['oauth_token_secret']
    )
    # 请求 access_token
    access_token_url = BASE_URL + 'oauth/access_token'
    access_token = oauth.fetch_access_token(access_token_url)
    return __import__('django').http.HttpResponse(access_token['oauth_token'])
