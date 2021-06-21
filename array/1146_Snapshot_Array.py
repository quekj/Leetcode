class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.length = length
        self.dic = {}
        self.snap_id = 0

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index >= 0 and index < self.length:
            self.dic[(index, self.snap_id)] = val

    def snap(self):
        """
        :rtype: int
        """
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        
        while snap_id >= 0:
            if (index,snap_id) in self.dic:
                return self.dic[(index,snap_id)]
            else:
                snap_id -= 1
        return 0

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
