# -*- coding: utf-8 -*-
import logging
from functools import partial
import json
import os

from rest_framework.response import Response
from rest_framework.views import APIView, exception_handler
from app.dbmodels import models
from app.data_utils import get_player_data
LOGGER = logging.getLogger('django')


class PlayerSummary(APIView):
    logger = LOGGER

    def get(self, request, playerID):
        try:
            player_data = get_player_data(playerID)
            if player_data is not None:
                return Response(player_data)
            else:
                return Response({"error": "Player not found"}, status=404)
        except Exception as e:
            return Response({"error": "An error has occurred"}, status=500)
