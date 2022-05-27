from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Une permission propre à un utilisateur qui peut modifier l'objet
    """

    def has_object_permission(self, request, view, obj):
        # Les autorisations de lecture sont accordées à toute demande,
        # nous autoriserons donc toujours les requêtes GET, HEAD ou OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Les autorisations d'écriture ne sont accordées qu'au propriétaire de l'extrait de code.
        return obj.owner == request.user