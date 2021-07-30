from django.test import TestCase
from .models import Article
from django.contrib.auth import get_user_model
User = get_user_model()

class ArticleTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(('username', 'Pas$w0rd'))
        Article.objects.create(author='Abdulla', title='Intern', email='prosto@gmail.com', owner=user)

    def test_article_author(self):
        author = Article.objects.get(author='Abdulla')
        self.assertEqual(author.author, 'Abdulla')

    def test_article_title(self):
        owner = Article.objects.get(title='Intern')
        self.assertEqual(owner.title, "Intern")

    def test_article_email(self):
        mail = Article.objects.get(email='prosto@gmail.com')
        self.assertEqual(mail.author, "Abdulla")

    def test_not_article_owner(self):
        owner = Article.objects.get(author='Abdulla')
        self.assertNotEqual(owner.author, "bot")

    def test_not_article_owner_id(self):
        id = Article.objects.get(id=1)
        self.assertNotEqual(id.id, 10)

    def test_id_is_not_real_user(self):
        user = User.objects.get()
        self.assertNotEqual(user.id, 2)

    def test_is_not_user(self):
        user = User.objects.get()
        self.assertNotEqual(user.username, "bot")




    # author = models.CharField(max_length=100)
    # title = models.CharField(max_length=100)
    # email = models.EmailField(max_length=100)
    # date = models.DateTimeField(auto_now_add=True)
    # highlighted = models.TextField()
    # owner = models.ForeignKey('auth.User', related_name='articles', on_delete=models.CASCADE)