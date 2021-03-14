from bobs_bus import bus, logger, bobs_id
from responses import BobResponse
import asyncio
import json
import sys
import logging


logger.setLevel(logging.DEBUG)

async def message_handler(message):
    msg = json.loads(message)
    if 'event' in msg and msg['event'] == 'posted' and 'mentions' in msg['data'] and bobs_id in msg['data']['mentions']:
        post = json.loads(msg['data']['post'])
        channel_id = post['channel_id']
        
        logger.debug("In Func")
        req = BobResponse(bus, channel_id, post)
        res = req.parse_response()
        logger.info(f"RES -> {json.dumps(res, indent=2)}")
        
    else:
        logger.debug(json.dumps(msg, indent=2))

bus.init_websocket(message_handler)