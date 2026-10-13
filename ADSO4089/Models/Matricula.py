class Matricula:

    def __init__(self, MAT_ID, MAT_UUID, MAT_ESTADO, MAT_FECHA_INSCRIPCION, MAT_APR_ID, MAT_CUR_ID):
        self.__MAT_ID                = MAT_ID
        self.__MAT_UUID              = MAT_UUID
        self.__MAT_ESTADO            = MAT_ESTADO
        self.__MAT_FECHA_INSCRIPCION = MAT_FECHA_INSCRIPCION
        self.__MAT_APR_ID            = MAT_APR_ID
        self.__MAT_CUR_ID            = MAT_CUR_ID

    def to_dict(self):
        return {
            "MAT_ID": self.__MAT_ID,
            "MAT_UUID": self.__MAT_UUID,
            "MAT_ESTADO": self.__MAT_ESTADO,
            "MAT_FECHA_INSCRIPCION": self.__MAT_FECHA_INSCRIPCION,
            "MAT_APR_ID": self.__MAT_APR_ID,
            "MAT_CUR_ID": self.__MAT_CUR_ID
        }
