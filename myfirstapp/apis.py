from .models import SampleModel                          # モデル呼出
from rest_framework.generics import ListAPIView    # API（変更)
from .serializers import SampleSerializer                # APIで渡すデータをJSON,XML変換

class api(ListAPIView):
    # 対象とするモデルのオブジェクトを定義
    queryset = SampleModel.objects.all()

    # APIがデータを返すためのデータ変換ロジックを定義
    serializer_class = SampleSerializer

    # 認証
    permission_classes = []