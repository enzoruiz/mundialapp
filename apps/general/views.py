from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Equipo, Encuentro

# Create your views here.

class InicioView(TemplateView):
	def get(self, request, *args, **kwargs):
		encuentros = Encuentro.objects.all().exclude(goleslocal__isnull=True)

		resultados = {
			"BRASILPJ" : 0,
			"BRASILGF" : 0,
			"BRASILGC" : 0,
			"BRASILPT" : 0,
			"CROACIAPJ" : 0,
			"CROACIAGF" : 0,
			"CROACIAGC" : 0,
			"CROACIAPT" : 0,
			"MEXICOPJ" : 0,
			"MEXICOGF" : 0,
			"MEXICOGC" : 0,
			"MEXICOPT" : 0,
			"CAMERUNPJ" : 0,
			"CAMERUNGF" : 0,
			"CAMERUNGC" : 0,
			"CAMERUNPT" : 0,
			"ESPAÑAPJ" : 0,
			"ESPAÑAGF" : 0,
			"ESPAÑAGC" : 0,
			"ESPAÑAPT" : 0,
			"HOLANDAPJ" : 0,
			"HOLANDAGF" : 0,
			"HOLANDAGC" : 0,
			"HOLANDAPT" : 0,
			"CHILEPJ" : 0,
			"CHILEGF" : 0,
			"CHILEGC" : 0,
			"CHILEPT" : 0,
			"AUSTRALIAPJ" : 0,
			"AUSTRALIAGF" : 0,
			"AUSTRALIAGC" : 0,
			"AUSTRALIAPT" : 0,
			"COLOMBIAPJ" : 0,
			"COLOMBIAGF" : 0,
			"COLOMBIAGC" : 0,
			"COLOMBIAPT" : 0,
			"GRECIAPJ" : 0,
			"GRECIAGF" : 0,
			"GRECIAGC" : 0,
			"GRECIAPT" : 0,
			"COSTADEMARFILPJ" : 0,
			"COSTADEMARFILGF" : 0,
			"COSTADEMARFILGC" : 0,
			"COSTADEMARFILPT" : 0,
			"JAPONPJ" : 0,
			"JAPONGF" : 0,
			"JAPONGC" : 0,
			"JAPONPT" : 0,
			"URUGUAYPJ" : 0,
			"URUGUAYGF" : 0,
			"URUGUAYGC" : 0,
			"URUGUAYPT" : 0,
			"COSTARICAPJ" : 0,
			"COSTARICAGF" : 0,
			"COSTARICAGC" : 0,
			"COSTARICAPT" : 0,
			"INGLATERRAPJ" : 0,
			"INGLATERRAGF" : 0,
			"INGLATERRAGC" : 0,
			"INGLATERRAPT" : 0,
			"ITALIAPJ" : 0,
			"ITALIAGF" : 0,
			"ITALIAGC" : 0,
			"ITALIAPT" : 0,
			"SUIZAPJ" : 0,
			"SUIZAGF" : 0,
			"SUIZAGC" : 0,
			"SUIZAPT" : 0,
			"ECUADORPJ" : 0,
			"ECUADORGF" : 0,
			"ECUADORGC" : 0,
			"ECUADORPT" : 0,
			"FRANCIAPJ" : 0,
			"FRANCIAGF" : 0,
			"FRANCIAGC" : 0,
			"FRANCIAPT" : 0,
			"HONDURASPJ" : 0,
			"HONDURASGF" : 0,
			"HONDURASGC" : 0,
			"HONDURASPT" : 0,
			"ARGENTINAPJ" : 0,
			"ARGENTINAGF" : 0,
			"ARGENTINAGC" : 0,
			"ARGENTINAPT" : 0,
			"BOSNIAPJ" : 0,
			"BOSNIAGF" : 0,
			"BOSNIAGC" : 0,
			"BOSNIAPT" : 0,
			"IRANPJ" : 0,
			"IRANGF" : 0,
			"IRANGC" : 0,
			"IRANPT" : 0,
			"NIGERIAPJ" : 0,
			"NIGERIAGF" : 0,
			"NIGERIAGC" : 0,
			"NIGERIAPT" : 0,
			"ALEMANIAPJ" : 0,
			"ALEMANIAGF" : 0,
			"ALEMANIAGC" : 0,
			"ALEMANIAPT" : 0,
			"PORTUGALPJ" : 0,
			"PORTUGALGF" : 0,
			"PORTUGALGC" : 0,
			"PORTUGALPT" : 0,
			"GHANAPJ" : 0,
			"GHANAGF" : 0,
			"GHANAGC" : 0,
			"GHANAPT" : 0,
			"ESTADOSUNIDOSPJ" : 0,
			"ESTADOSUNIDOSGF" : 0,
			"ESTADOSUNIDOSGC" : 0,
			"ESTADOSUNIDOSPT" : 0,
			"BELGICAPJ" : 0,
			"BELGICAGF" : 0,
			"BELGICAGC" : 0,
			"BELGICAPT" : 0,
			"ARGELIAPJ" : 0,
			"ARGELIAGF" : 0,
			"ARGELIAGC" : 0,
			"ARGELIAPT" : 0,
			"RUSIAPJ" : 0,
			"RUSIAGF" : 0,
			"RUSIAGC" : 0,
			"RUSIAPT" : 0,
			"COREADELSURPJ" : 0,
			"COREADELSURGF" : 0,
			"COREADELSURGC" : 0,
			"COREADELSURPT" : 0,
		}

		for encuentro in encuentros:
			GF = encuentro.goleslocal
			GC = encuentro.golesvisita
			if GF > GC:
				PTL = 3
				PTV = 0
			elif GF < GC:
				PTL = 0
				PTV = 3
			else:
				PTL = 1
				PTV = 1
			
			local = encuentro.local.pais
			visita = encuentro.visita.pais
			local = local.replace(' ', '')
			visita = visita.replace(' ', '')

			resultados[local+'PJ'] += 1
			resultados[local+'GF'] += GF
			resultados[local+'GC'] += GC
			resultados[local+'PT'] += PTL

			resultados[visita+'PJ'] += 1
			resultados[visita+'GF'] += GC
			resultados[visita+'GC'] += GF
			resultados[visita+'PT'] += PTV

		Equipo.objects.filter(pais='BRASIL').update(pj=resultados["BRASILPJ"], gf=resultados["BRASILGF"], gc=resultados["BRASILGC"], df=resultados["BRASILGF"]-resultados["BRASILGC"], pt=resultados["BRASILPT"])
		Equipo.objects.filter(pais='CROACIA').update(pj=resultados["CROACIAPJ"], gf=resultados["CROACIAGF"], gc=resultados["CROACIAGC"], df=resultados["CROACIAGF"]-resultados["CROACIAGC"], pt=resultados["CROACIAPT"])
		Equipo.objects.filter(pais='MEXICO').update(pj=resultados["MEXICOPJ"], gf=resultados["MEXICOGF"], gc=resultados["MEXICOGC"], df=resultados["MEXICOGF"]-resultados["MEXICOGC"], pt=resultados["MEXICOPT"])
		Equipo.objects.filter(pais='CAMERUN').update(pj=resultados["CAMERUNPJ"], gf=resultados["CAMERUNGF"], gc=resultados["CAMERUNGC"], df=resultados["CAMERUNGF"]-resultados["CAMERUNGC"], pt=resultados["CAMERUNPT"])

		Equipo.objects.filter(pais='ESPAÑA').update(pj=resultados["ESPAÑAPJ"], gf=resultados["ESPAÑAGF"], gc=resultados["ESPAÑAGC"], df=resultados["ESPAÑAGF"]-resultados["ESPAÑAGC"], pt=resultados["ESPAÑAPT"])
		Equipo.objects.filter(pais='HOLANDA').update(pj=resultados["HOLANDAPJ"], gf=resultados["HOLANDAGF"], gc=resultados["HOLANDAGC"], df=resultados["HOLANDAGF"]-resultados["HOLANDAGC"], pt=resultados["HOLANDAPT"])
		Equipo.objects.filter(pais='CHILE').update(pj=resultados["CHILEPJ"], gf=resultados["CHILEGF"], gc=resultados["CHILEGC"], df=resultados["CHILEGF"]-resultados["CHILEGC"], pt=resultados["CHILEPT"])
		Equipo.objects.filter(pais='AUSTRALIA').update(pj=resultados["AUSTRALIAPJ"], gf=resultados["AUSTRALIAGF"], gc=resultados["AUSTRALIAGC"], df=resultados["AUSTRALIAGF"]-resultados["AUSTRALIAGC"], pt=resultados["AUSTRALIAPT"])

		Equipo.objects.filter(pais='COLOMBIA').update(pj=resultados["COLOMBIAPJ"], gf=resultados["COLOMBIAGF"], gc=resultados["COLOMBIAGC"], df=resultados["COLOMBIAGF"]-resultados["COLOMBIAGC"], pt=resultados["COLOMBIAPT"])
		Equipo.objects.filter(pais='GRECIA').update(pj=resultados["GRECIAPJ"], gf=resultados["GRECIAGF"], gc=resultados["GRECIAGC"], df=resultados["GRECIAGF"]-resultados["GRECIAGC"], pt=resultados["GRECIAPT"])
		Equipo.objects.filter(pais='COSTA DE MARFIL').update(pj=resultados["COSTADEMARFILPJ"], gf=resultados["COSTADEMARFILGF"], gc=resultados["COSTADEMARFILGC"], df=resultados["COSTADEMARFILGF"]-resultados["COSTADEMARFILGC"], pt=resultados["COSTADEMARFILPT"])
		Equipo.objects.filter(pais='JAPON').update(pj=resultados["JAPONPJ"], gf=resultados["JAPONGF"], gc=resultados["JAPONGC"], df=resultados["JAPONGF"]-resultados["JAPONGC"], pt=resultados["JAPONPT"])

		Equipo.objects.filter(pais='URUGUAY').update(pj=resultados["URUGUAYPJ"], gf=resultados["URUGUAYGF"], gc=resultados["URUGUAYGC"], df=resultados["URUGUAYGF"]-resultados["URUGUAYGC"], pt=resultados["URUGUAYPT"])
		Equipo.objects.filter(pais='COSTA RICA').update(pj=resultados["COSTARICAPJ"], gf=resultados["COSTARICAGF"], gc=resultados["COSTARICAGC"], df=resultados["COSTARICAGF"]-resultados["COSTARICAGC"], pt=resultados["COSTARICAPT"])
		Equipo.objects.filter(pais='INGLATERRA').update(pj=resultados["INGLATERRAPJ"], gf=resultados["INGLATERRAGF"], gc=resultados["INGLATERRAGC"], df=resultados["INGLATERRAGF"]-resultados["INGLATERRAGC"], pt=resultados["INGLATERRAPT"])
		Equipo.objects.filter(pais='ITALIA').update(pj=resultados["ITALIAPJ"], gf=resultados["ITALIAGF"], gc=resultados["ITALIAGC"], df=resultados["ITALIAGF"]-resultados["ITALIAGC"], pt=resultados["ITALIAPT"])

		Equipo.objects.filter(pais='SUIZA').update(pj=resultados["SUIZAPJ"], gf=resultados["SUIZAGF"], gc=resultados["SUIZAGC"], df=resultados["SUIZAGF"]-resultados["SUIZAGC"], pt=resultados["SUIZAPT"])
		Equipo.objects.filter(pais='ECUADOR').update(pj=resultados["ECUADORPJ"], gf=resultados["ECUADORGF"], gc=resultados["ECUADORGC"], df=resultados["ECUADORGF"]-resultados["ECUADORGC"], pt=resultados["ECUADORPT"])
		Equipo.objects.filter(pais='FRANCIA').update(pj=resultados["FRANCIAPJ"], gf=resultados["FRANCIAGF"], gc=resultados["FRANCIAGC"], df=resultados["FRANCIAGF"]-resultados["FRANCIAGC"], pt=resultados["FRANCIAPT"])
		Equipo.objects.filter(pais='HONDURAS').update(pj=resultados["HONDURASPJ"], gf=resultados["HONDURASGF"], gc=resultados["HONDURASGC"], df=resultados["HONDURASGF"]-resultados["HONDURASGC"], pt=resultados["HONDURASPT"])

		Equipo.objects.filter(pais='ARGENTINA').update(pj=resultados["ARGENTINAPJ"], gf=resultados["ARGENTINAGF"], gc=resultados["ARGENTINAGC"], df=resultados["ARGENTINAGF"]-resultados["ARGENTINAGC"], pt=resultados["ARGENTINAPT"])
		Equipo.objects.filter(pais='BOSNIA').update(pj=resultados["BOSNIAPJ"], gf=resultados["BOSNIAGF"], gc=resultados["BOSNIAGC"], df=resultados["BOSNIAGF"]-resultados["BOSNIAGC"], pt=resultados["BOSNIAPT"])
		Equipo.objects.filter(pais='IRAN').update(pj=resultados["IRANPJ"], gf=resultados["IRANGF"], gc=resultados["IRANGC"], df=resultados["IRANGF"]-resultados["IRANGC"], pt=resultados["IRANPT"])
		Equipo.objects.filter(pais='NIGERIA').update(pj=resultados["NIGERIAPJ"], gf=resultados["NIGERIAGF"], gc=resultados["NIGERIAGC"], df=resultados["NIGERIAGF"]-resultados["NIGERIAGC"], pt=resultados["NIGERIAPT"])

		Equipo.objects.filter(pais='ALEMANIA').update(pj=resultados["ALEMANIAPJ"], gf=resultados["ALEMANIAGF"], gc=resultados["ALEMANIAGC"], df=resultados["ALEMANIAGF"]-resultados["ALEMANIAGC"], pt=resultados["ALEMANIAPT"])
		Equipo.objects.filter(pais='PORTUGAL').update(pj=resultados["PORTUGALPJ"], gf=resultados["PORTUGALGF"], gc=resultados["PORTUGALGC"], df=resultados["PORTUGALGF"]-resultados["PORTUGALGC"], pt=resultados["PORTUGALPT"])
		Equipo.objects.filter(pais='GHANA').update(pj=resultados["GHANAPJ"], gf=resultados["GHANAGF"], gc=resultados["GHANAGC"], df=resultados["GHANAGF"]-resultados["GHANAGC"], pt=resultados["GHANAPT"])
		Equipo.objects.filter(pais='ESTADOS UNIDOS').update(pj=resultados["ESTADOSUNIDOSPJ"], gf=resultados["ESTADOSUNIDOSGF"], gc=resultados["ESTADOSUNIDOSGC"], df=resultados["ESTADOSUNIDOSGF"]-resultados["ESTADOSUNIDOSGC"], pt=resultados["ESTADOSUNIDOSPT"])

		Equipo.objects.filter(pais='BELGICA').update(pj=resultados["BELGICAPJ"], gf=resultados["BELGICAGF"], gc=resultados["BELGICAGC"], df=resultados["BELGICAGF"]-resultados["BELGICAGC"], pt=resultados["BELGICAPT"])
		Equipo.objects.filter(pais='ARGELIA').update(pj=resultados["ARGELIAPJ"], gf=resultados["ARGELIAGF"], gc=resultados["ARGELIAGC"], df=resultados["ARGELIAGF"]-resultados["ARGELIAGC"], pt=resultados["ARGELIAPT"])
		Equipo.objects.filter(pais='RUSIA').update(pj=resultados["RUSIAPJ"], gf=resultados["RUSIAGF"], gc=resultados["RUSIAGC"], df=resultados["RUSIAGF"]-resultados["RUSIAGC"], pt=resultados["RUSIAPT"])
		Equipo.objects.filter(pais='COREA DEL SUR').update(pj=resultados["COREADELSURPJ"], gf=resultados["COREADELSURGF"], gc=resultados["COREADELSURGC"], df=resultados["COREADELSURGF"]-resultados["COREADELSURGC"], pt=resultados["COREADELSURPT"])

		grupoa = Equipo.objects.filter(grupo__letra='A').order_by('-pt', '-df')
		grupob = Equipo.objects.filter(grupo__letra='B').order_by('-pt', '-df')
		grupoc = Equipo.objects.filter(grupo__letra='C').order_by('-pt', '-df')
		grupod = Equipo.objects.filter(grupo__letra='D').order_by('-pt', '-df')
		grupoe = Equipo.objects.filter(grupo__letra='E').order_by('-pt', '-df')
		grupof = Equipo.objects.filter(grupo__letra='F').order_by('-pt', '-df')
		grupog = Equipo.objects.filter(grupo__letra='G').order_by('-pt', '-df')
		grupoh = Equipo.objects.filter(grupo__letra='H').order_by('-pt', '-df')

		return render(request, 'general/inicio.html', {'grupoa' : grupoa, 'grupob' : grupob, 'grupoc' : grupoc, 'grupod' : grupod, 'grupoe' : grupoe, 'grupof' : grupof, 'grupog' : grupog, 'grupoh' : grupoh})