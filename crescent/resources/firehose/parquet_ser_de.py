from crescent.core import Model
from .constants import AllowedValues


class ParquetSerDe(Model):
    def __init__(self):
        super(ParquetSerDe, self).__init__(
            min_value={self.BlockSizeBytes.__name__: 67108864,
                       self.MaxPaddingBytes.__name__: 0,
                       self.PageSizeBytes.__name__: 65536},
            allowed_values={self.Compression.__name__: AllowedValues.PARQUET_SER_DE_COMPRESSION,
                            self.WriterVersion.__name__: AllowedValues.PARQUET_SER_DE_WRITER_VERSION}
        )

    def BlockSizeBytes(self, block_size_bytes: int):
        return self._set_field(self.BlockSizeBytes.__name__, block_size_bytes)

    def Compression(self, compression: str):
        return self._set_field(self.Compression.__name__, compression)

    def EnableDictionaryCompression(self, enable_dict_compression: bool):
        return self._set_field(self.EnableDictionaryCompression.__name__, enable_dict_compression)

    def MaxPaddingBytes(self, max_padding_bytes: int):
        return self._set_field(self.MaxPaddingBytes.__name__, max_padding_bytes)

    def PageSizeBytes(self, page_size_bytes: int):
        return self._set_field(self.PageSizeBytes.__name__, page_size_bytes)

    def WriterVersion(self, writer_version: str):
        return self._set_field(self.WriterVersion.__name__, writer_version)
