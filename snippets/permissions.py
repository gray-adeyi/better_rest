from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only owners of an 
    object edit it.
    """
    
    def object_has_permission(self, request, view, obj): 
        # read permissions are allowed to any request,
        # sow we'll allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # write permissions are only allowed to the owner of the
        # snippet. 
        return obj.owner == request.user 
