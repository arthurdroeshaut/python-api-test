# python-api-test

Algemene Eisen en Documentatie:


Documentatie van mijn StarWars Randomizer.
Ik heb als onderwerp gekozen voor StarWars, ik heb hiervoor enkele personages uit films en series gebruikt, verschillende kleuren van lichtzwaarden, verschillende soorten in het star wars universum, bepaalde planeten als geboorteplaatsen, en verschillende ranks zowel jedi als sith ranks in eenzelfde "Ranks" lijst en bepaalde schepen als mogelijke schepen.
zoals in de screenshot die je hier ziet:

![screenshot starwars](https://user-images.githubusercontent.com/61418112/202923053-66c1f409-d187-4ca1-b8ff-4d935b5416b6.png)

dit is al de beschrijving van mijn gekozen API onderwerp nu verder naar de API.
de nodige links:
hier de link van mijn API in github: https://github.com/arthurdroeshaut/python-api-test

hier de link van mijn Frontend in github: https://github.com/arthurdroeshaut/API-Frontend

en hier de link naar mijn hosted frontend: https://arthurdroeshaut.github.io/API-Frontend/

REST API:
nu ga ik aantonen dat mijn get-requests en mijn Post-request werken op postman.
hieronder mijn eerste get-request, dit was een simpel request dat een random Star_Wars_Character moet tonen uit de lijst

![image](https://user-images.githubusercontent.com/61418112/202923484-bd2e9a86-ebce-4c89-89e1-934628686efb.png)

zoals je ziet werkt dit goed en krijg je altijd een random karakter uit de lijst, dit is de gebruikte code voor deze get-request.

![image](https://user-images.githubusercontent.com/61418112/202923699-963156ae-ed48-4ee8-b587-3caff98c5db2.png)

ik heb deze get-requests ook nog gedaan voor de andere lijsten: dat zijn dus al mijn get-requests exclusief de eerste.

![image](https://user-images.githubusercontent.com/61418112/202923849-1cc58600-30ce-4c7d-9fbc-c16c0bf6cc69.png)

ik zal ook een tweede tonen in postman, hiervoor kies ik de random Rank get-request.

![image](https://user-images.githubusercontent.com/61418112/202924401-34d8bbbc-de09-4a68-955e-5f55028f2bf5.png)

aangezien er in de documentatie gevraagd wordt voor totale werking API door screenshots zal ik alle rest ook maar erin zetten.
species:

![image](https://user-images.githubusercontent.com/61418112/202924461-fe98757f-26e1-459d-b3fe-4514344206d5.png)

Birthplace:

![image](https://user-images.githubusercontent.com/61418112/202924473-878cd11b-0268-45e9-851d-181dec2ea7a2.png)

LightsaberColor:

![image](https://user-images.githubusercontent.com/61418112/202924508-44daa9a6-7d0f-4959-ae76-e524e6c40aac.png)

en als laatste get: Ship:

![image](https://user-images.githubusercontent.com/61418112/202924533-c8b900c4-bc9f-40c1-b5f9-b0e4d19d18a7.png)

hieronder komt de werking van mijn Post request met de code van mijn post request te staan
code: (in deze code staat lightsabercolor, rank en ship anders want deze kunnen ook none dus leeggelaten worden. (want niet ieder karakter heeft een lightsaber, ship of rang.)

![image](https://user-images.githubusercontent.com/61418112/202924566-b0bc800e-4e3e-4112-8de2-f9dd139f5b2a.png)

en in postman ziet dit er zo uit:

![image](https://user-images.githubusercontent.com/61418112/202924703-00545257-f748-480a-8708-438d3c955337.png)

zoals je kan zien maak ik een nieuwe character aan, eentje die nog niet uit de lijst komt, want dat is ook mogelijk, en geef ik alle rest ook mee sommigen dingen zitten al in de lijst anderen niet.

dus ik heb nu al mijn Github reposity gedocumenteerd (API & Front-end)
beschrijving van mijn thema, je api en front end en links naar hosted API.
6 get endpoints getoond en mijn post endpoint ook getoond.
dus nu door naar deployment

Deployment: Docker container voor de API is ook terug te vinden in de github repository en deze worden automatisch opgebouwd in github actions:

![image](https://user-images.githubusercontent.com/61418112/202925076-9e263492-d719-4c61-8222-8bb31724b609.png)

nu verder nog de deployment van de API container op okteto cloud via docker compose, hiervoor hebben wel al een docker compose file nodig, deze staat ook in de github repository.
de stappen die je hiervoor moet volgen zijn vrij simpel en waarschijnlijk doe ik er zelfs teveel:

"commando's voor docker login push etc voor API DEV
na aanmaken dockerfile: 

docker login

docker build -t r0750378/python-api-test:latest .
of
docker build -t r0750378/python-api-test:latest https://github.com/arthurdroeshaut/python-api-test.git#main

docker push -q r0750378/python-api-test

hierna moet je de docker container deployen met docker compose en een docker-compose.yml file

docker compose up na het maken van de file. op de plaats waar je bestanden en docker-compose.yml file staat.

hierna deployen we de file naar de okteto cloud.
"
dit ziet er zo uit:

![image](https://user-images.githubusercontent.com/61418112/202925192-cfae9431-4da9-4f08-b3b6-4d0fe26816f7.png)

![image](https://user-images.githubusercontent.com/61418112/202925264-0affff35-f178-45a5-82e2-7765f7406d1c.png)

ga naar de site van okteto
en klik op launch dev environment.
klik op github & klik op de juiste repository.

dit was dan het deployment gedeelte.
nu over naar het front-end gedeelte:

de website ziet er als volgt uit:
ik kan wel aanraden om de website op 75-80% grootte te zetten

![image](https://user-images.githubusercontent.com/61418112/202925419-129e542e-9a1d-40e8-897e-53204beda313.png)


en deze code kan je vinden in het frontend gedeelde op deze link: https://github.com/arthurdroeshaut/API-Frontend (2e keer dat deze link erin staat)

