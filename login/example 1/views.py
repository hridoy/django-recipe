def signin(request):

    if request.user.is_authenticated:
        return render(request, '/')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'pages/account/login.html', {})
    else:
        return render(request, 'pages/account/login.html', {})