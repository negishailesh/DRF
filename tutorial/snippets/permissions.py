from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
	'''
	custom permission to oly allow owners of an object to edit it.
	
	'''
	def has_object_permission(self , request , view, obj):
		#Read permission are allowed to any request,
		#so we'll allow GET,HEAD or OPTION requests.
		
		if request.method in permissions.SAFE_METHODS:
			return True

		#write permission are only allowed to the owner of the snippet

		return obj.owner == request.user



