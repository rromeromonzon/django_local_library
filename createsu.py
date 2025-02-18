from django.contrib.auth import get_user_model


User = get_user_model()

if not User.objects.filter(username='alumnodb').exists():
    User.objects.create_superuser('alumnodb', '', 'alumnodb')
    print('Superuser created')
else:
    print('Superuser alumnodb already exists')