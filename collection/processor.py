from collection.models import Collection

def get_collection_list(request):
	collections = Collection.objects.all().order_by('-pub_date')
	return {'collections':collections}
