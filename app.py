#@app.route("/home")
#def home():
#    return render_template("index.html")
#
#
#
#
#@app.route("/chat",methods=['GET'])
#def chat():
#    pdb.set_trace()
#    while True:
#        
#        inp=request.args['user_input']
#        #    inp = input("You: ")
#        
#       
#        if inp.lower() == "quit":
#            break
#        
#        if 'dolar' in inp:
#            cmd.exchangeDolar()
#            
#        if 'euro' in inp:
#            cmd.exchangeEuro()
#            
#        if 'google aç' in inp:
#            cmd.openBrowser()
#            
#        if 'çeviri' in inp:
#            cmd.openTranslate()
#            
#        if 'hava durumu' in inp:
#            cmd.weather()
#            
#        if 'harita' in inp:
#            cmd.maps()   
#           
#            
#        
#        results = model.predict([bag_of_words(inp,words)])
#        results_index =  numpy.argmax(results)
#        tag=labels[results_index]
#       
#        for tg in data["intents"]:
#            if tg['tag'] == tag:
#                responses = tg['responses']
#                
#        responce= random.choice(responses)
#        bot_response=str(responce)
#        user_input=str(inp)
#        return render_template('index.html',inp=user_input,
#		responce=bot_response)
#        
#        
##        return responce
#   
#
#
#if __name__ == "__main__":
#    app.run(debug=True,port=5000) 
#        
        
        