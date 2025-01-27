from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView

# criar: url - view - html

# Create your views here.
class Homepage(TemplateView):
    template_name = "homepage.html"
    
    
class Homefilmes(ListView):  # <========= o objetivo dessa classe é exibir uma lista de filmes (uma lista de objetos no banco de dados) 
# então quando vc tem uma view cujo objetivo é exibir uma lista de itens do seu banco de dados vc pode importar de uma listView
# Uma list View  espera que voce passe 2 informações, o template_name e o modelo
    template_name = "homefilmes.html"
    model =  Filme    # <======== model é o modelo do banco de dados que eu vou pegar a minha lista. 
    # Com o uso do listview e do model ele vai me retornar uma object_list, esse object_list eu devo passar para o html da pagina especifica, no caso "Homefilmes"


#  vai criar uma pagina para cada filme
class Detalhesfilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    # no listview ele retornava uma lista,  e a variavel digamos a ser renderizada no html era object_list
    # no detailview, a variavel a ser renderizada no html será o object (apenas 1 item)
    
    def get(self,request,*args,**kwargs): # <====== por padrão o get recebe esses 4 argumentos
    # a função get vai retornar ao usuário o link que ela está querendo acessar
    
        # descobrir qual filme ele está acessando:
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()   # <===== salva a modificação no banco de dados
        return super(Detalhesfilme, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria = self.get_object().categoria)[0:5]  # <====== essa linha está pegando os objects da classe Filmes, no caso pegando 5 filmes cuja categoria são relacionadas com o filme escolhido
        context['filmes_relacionados'] = filmes_relacionados
        return context









# def homepage(request):
#     return render(request, "homepage.html")  # <============ precisa ser passado 2 parametros, 1 - REQUEST, 2 - NOME DO TEMPLATE

# def homefilmes(request):
#     context = {}                                       # <============ context é um dicionário python
#     lista_filmes = Filme.objects.all()                 # <============ PEGANDO INFORMAÇÕES DO BANCO DE DADOS 
#     context['lista_filmes'] = lista_filmes             # <============ criei uma chave lista_filmes e estou atribuindo valor a essa chave
#     return render(request, "homefilmes.html", context) # <============ Na função render posso passar um novo parametro, que é o context



    