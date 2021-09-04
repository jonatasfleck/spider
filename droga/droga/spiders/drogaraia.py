import scrapy

class DrogaraiaSpider(scrapy.Spider):
    name = 'drogaraia'
    
    start_urls = [f'https://www.drogaraia.com.br/medicamentos/remedios/genericos.html?p={i}' for i in range(1,8)] 
    #Limite de páginas especificados, pode se adicionar um next_page com o link para a próxima página, sendo necessário inserir o request para o start_urls e o callback para o parse.
     

    def parse(self, response, **kwargs): # Foi utilizado o *Kwargs para nomear vários parâmetros.
        for i in response.xpath('//div[@class="container"]'): #Div da lista de produtos, dentro desta DIV podemos encontrar link para o produto, nome do produto, old price e new price(ou special price), e etc.  
            link = i.xpath('./a/@href').get() #Parâmetro para a captura do link das ofertas. 
            name = i.xpath('./a/@title').get() #Parâmetro para a captura do nome das ofertas.

            yield{ #Foi utilizado o Yield para coletar os dados pelo motivo de ele não armazenar os dados coletados na memória, como podemos capturar inúmeras páginas o uso dele nos ajuda a economizar memória. 
                'link' : link,  # return do parse link
                'name' : name   # return do parse name             
                
            }

# Arquivo da captura foi salvo em 2 formatos(JSON e XML), pois o nome quando convertido para JSON estava me devolvendo sem acentos. 
 # Ajustes realizados no settings.py:
 # 1. Foi definido o USER_AGENT para o site nos identificar como um navegador autêntico 
 # 2. Foi definido o AUTO_THROTLE do spider como TRUE, para obtermos um delay em cada requisição (este pode ser comentado em settings para termos requisições mais rápidas, com o risco de sermos bloqueados pelo site minerado).           
 # 3. Foi definido o ROBOTSTXT_OBEY como FALSE pois este estava bloqueando a captura da página.  

#Futuramente será desenvolvida uma interface para facilitar a configuração da captura de cada página específica, com mais parâmetros de captura. 
#Código desenvolvido por Jonatas Fleck, para realizar testes de captura de páginas. 
            
