end= '\33[0m';bold= '\33[1m';italic='\33[3m';underline= '\33[4m';highlight= '\33[7m';black= '\33[30m';red= '\33[31m';green= '\33[32m';yellow= '\33[33m';blue= '\33[34m';violet= '\33[35m';beige = '\33[36m';white  = '\33[37m';blackh= '\33[40m';redh= '\33[41m';greenh= '\33[42m';yellowh= '\33[43m';blueh= '\33[44m';violeth= '\33[45m';beigeh= '\33[46m';whiteh= '\33[47m';grey = '\33[90m';red2= '\33[91m';green2= '\33[92m';yellow2= '\33[93m';blue2= '\33[94m';violet2= '\33[95m';beige2= '\33[96m';white2= '\33[97m'
def printc(text, c=None,c_end=True, end=None, flush=False):
    endc= '\33[0m';bold= '\33[1m';italic='\33[3m';underline= '\33[4m';highlight= '\33[7m';black= '\33[30m';red= '\33[31m';green= '\33[32m';yellow= '\33[33m';blue= '\33[34m';violet= '\33[35m';beige = '\33[36m';white  = '\33[37m';blackh= '\33[40m';redh= '\33[41m';greenh= '\33[42m';yellowh= '\33[43m';blueh= '\33[44m';violeth= '\33[45m';beigeh= '\33[46m';whiteh= '\33[47m';grey = '\33[90m';red2= '\33[91m';green2= '\33[92m';yellow2= '\33[93m';blue2= '\33[94m';violet2= '\33[95m';beige2= '\33[96m';white2= '\33[97m'
    if c_end==True:
    	if c in locals() and c!='text' and c!='c_end' and c!='c':
    		a=locals()[c]
    		v=list(locals().values())
    		out=v.index(a)
    		out=v[out]
    		print(f'{out}'+text+f'{endc}', end=end, flush=flush)
    elif c_end==False:
    	if c in locals() and c!='text' and c!='c_end' and c!='c':
    		a=locals()[c]
    		v=list(locals().values())
    		out=v.index(a)
    		out=v[out]
    		print(f'{out}'+text, end=end, flush=flush)
def color(text, c=None):
    endc= '\33[0m';bold= '\33[1m';italic='\33[3m';underline= '\33[4m';highlight= '\33[7m';black= '\33[30m';red= '\33[31m';green= '\33[32m';yellow= '\33[33m';blue= '\33[34m';violet= '\33[35m';beige = '\33[36m';white  = '\33[37m';blackh= '\33[40m';redh= '\33[41m';greenh= '\33[42m';yellowh= '\33[43m';blueh= '\33[44m';violeth= '\33[45m';beigeh= '\33[46m';whiteh= '\33[47m';grey = '\33[90m';red2= '\33[91m';green2= '\33[92m';yellow2= '\33[93m';blue2= '\33[94m';violet2= '\33[95m';beige2= '\33[96m';white2= '\33[97m'
    if c in locals() and c!='text' and c!='c_end' and c!='c':
    	a=locals()[c]
    	v=list(locals().values())
    	out=v.index(a)
    	out=v[out]
    	return f'{out}'+text+f'{endc}'
if __name__=='__main__':
	print(color('hi', 'blue'))
	printc('hi', 'blue')
	print(f'{blue}hi{end}')