"""
HW05 — City Bike Registry (Resizing Chaining Map)
"""

class HashMap:
    """Chaining hash map with auto-resize at load factor > 0.75."""

    def __init__(self, m=4):
        # TODO: create m empty buckets and set size counter
        raise NotImplementedError

    def _hash(self, s):
        """Return simple integer hash for string s."""
        # TODO: sum character ordinals or similar
        raise NotImplementedError

    def _index(self, key, m=None):
        """Return bucket index for key with current or given bucket count."""
        # TODO
        raise NotImplementedError

    def __len__(self):
        """Return number of stored pairs."""
        # TODO
        raise NotImplementedError

    def _resize(self, new_m):
        """Resize to new_m buckets and rehash all pairs."""
        # TODO: allocate new buckets; reinsert all pairs
        raise NotImplementedError

    def put(self, key, value):
        """Insert or overwrite. Resize first if load will exceed 0.75."""
        # TODO: check load; maybe resize; then insert/overwrite
        raise NotImplementedError

    def get(self, key):
        """Return value for key or None if missing."""
        # TODO
        raise NotImplementedError

    def delete(self, key):
        """Remove key if present. Return True if removed else False."""
        # TODO
        raise NotImplementedError

if __name__ == "__main__":
    # Optional manual check
    pass
