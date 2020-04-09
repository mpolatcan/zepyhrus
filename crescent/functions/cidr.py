from .fn import FnArrayValue


class Cidr(FnArrayValue):
    def __init__(self):
        super(Cidr, self).__init__(
            fn_name=Cidr.__name__,
            field_order=[self.IpBlock.__name__, self.Count.__name__, self.CidrBits.__name__],
            min_value={self.Count.__name__: 1},
            max_value={self.Count.__name__: 256}
        )

    def IpBlock(self, ip_block: str):
        return self._set_field(self.IpBlock.__name__, ip_block)

    def Count(self, count: int):
        return self._set_field(self.Count.__name__, count)

    def CidrBits(self, cidr_bits: int):
        return self._set_field(self.CidrBits.__name__, cidr_bits)
