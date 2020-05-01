import inspect
from flask import request, jsonify
from API.Routes import dataSource, validateResponse, convertToJson, returnMissingParams, addtionalParams

import API.Stakeholder.lawyer as lawyer
from API import api

@api.route('/lawyer/getRequests', methods=['POST'])
def lawyer_getRequests():
    res = dataSource(request)
    params = inspect.getargspec(lawyer.getRequests).args

    # check params should be in res
    if (not validateResponse(params, res)):
        return jsonify({'res': 'failed', 'type':'missing params %s' %returnMissingParams(params, res)})
    
    if(not addtionalParams(params, res)):
        return jsonify({'res':'failed', 'reason': 'Additional Param Supplied.'})
    
    return convertToJson(lawyer.getRequests(**res))

@api.route('/lawyer/updateStatus', methods=['POST'])
def lawyer_updateStatus():
    res = dataSource(request)
    params = inspect.getargspec(lawyer.updateStatus).args

    # check params should be in res
    if (not validateResponse(params, res)):
        return jsonify({'res': 'failed', 'type':'missing params %s' %returnMissingParams(params, res)})
    
    if(not addtionalParams(params, res)):
        return jsonify({'res':'failed', 'reason': 'Additional Param Supplied.'})
    
    return convertToJson(lawyer.updateStatus(**res))

@api.route('/lawyer/attachAccusedLawyer', methods=['POST'])
def lawyer_attachAccusedLawyer():
    res = dataSource(request)
    params = inspect.getargspec(lawyer.attachAccusedLawyer).args

    # check params should be in res
    if (not validateResponse(params, res)):
        return jsonify({'res': 'failed', 'type':'missing params %s' %returnMissingParams(params, res)})
    
    if(not addtionalParams(params, res)):
        return jsonify({'res':'failed', 'reason': 'Additional Param Supplied.'})
    
    return convertToJson(lawyer.attachAccusedLawyer(**res))

@api.route('/lawyer/getPendingCases', methods=['POST'])
def lawyer_getPendingCases():
    res = dataSource(request)
    params = inspect.getargspec(lawyer.getPendingCases).args

    # check params should be in res
    if (not validateResponse(params, res)):
        return jsonify({'res': 'failed', 'type':'missing params %s' %returnMissingParams(params, res)})
    
    if(not addtionalParams(params, res)):
        return jsonify({'res':'failed', 'reason': 'Additional Param Supplied.'})
    
    return convertToJson(lawyer.getPendingCases(**res))

@api.route('/lawyer/getActiveCases', methods=['POST'])
def lawyer_getActiveCases():
    res = dataSource(request)
    params = inspect.getargspec(lawyer.getActiveCases).args

    # check params should be in res
    if (not validateResponse(params, res)):
        return jsonify({'res': 'failed', 'type':'missing params %s' %returnMissingParams(params, res)})
    
    if(not addtionalParams(params, res)):
        return jsonify({'res':'failed', 'reason': 'Additional Param Supplied.'})
    
    return convertToJson(lawyer.getActiveCases(**res))

@api.route('/lawyer/todaySchedule', methods=['POST'])
def lawyer_todaySchedule():
    res = dataSource(request)
    params = inspect.getargspec(lawyer.todaySchedule).args

    # check params should be in res
    if (not validateResponse(params, res)):
        return jsonify({'res': 'failed', 'type':'missing params %s' %returnMissingParams(params, res)})
    
    if(not addtionalParams(params, res)):
        return jsonify({'res':'failed', 'reason': 'Additional Param Supplied.'})
    
    return convertToJson(lawyer.todaySchedule(**res))

@api.route('/lawyer/getClosedCases', methods=['POST'])
def lawyer_getClosedCases():
    res = dataSource(request)
    params = inspect.getargspec(lawyer.getClosedCases).args

    # check params should be in res
    if (not validateResponse(params, res)):
        return jsonify({'res': 'failed', 'type':'missing params %s' %returnMissingParams(params, res)})
    
    if(not addtionalParams(params, res)):
        return jsonify({'res':'failed', 'reason': 'Additional Param Supplied.'})
    
    return convertToJson(lawyer.getClosedCases(**res))

@api.route('/lawyer/getPrevHearings', methods=['POST'])
def lawyer_getPrevHearings():
    res = dataSource(request)
    params = inspect.getargspec(lawyer.getPrevHearings).args

    # check params should be in res
    if (not validateResponse(params, res)):
        return jsonify({'res': 'failed', 'type':'missing params %s' %returnMissingParams(params, res)})
    
    if(not addtionalParams(params, res)):
        return jsonify({'res':'failed', 'reason': 'Additional Param Supplied.'})
    
    return convertToJson(lawyer.getPrevHearings(**res))

@api.route('/lawyer/getNotPaidClients', methods=['POST'])
def lawyer_getNotPaidClients():
    res = dataSource(request)
    params = inspect.getargspec(lawyer.getNotPaidClients).args

    # check params should be in res
    if (not validateResponse(params, res)):
        return jsonify({'res': 'failed', 'type':'missing params %s' %returnMissingParams(params, res)})
    
    if(not addtionalParams(params, res)):
        return jsonify({'res':'failed', 'reason': 'Additional Param Supplied.'})
    
    return convertToJson(lawyer.getNotPaidClients(**res))

@api.route('/lawyer/createPaymentRequest', methods=['POST'])
def lawyer_createPaymentRequest():
    res = dataSource(request)
    params = inspect.getargspec(lawyer.createPaymentRequest).args

    # check params should be in res
    if (not validateResponse(params, res)):
        return jsonify({'res': 'failed', 'type':'missing params %s' %returnMissingParams(params, res)})
    
    if(not addtionalParams(params, res)):
        return jsonify({'res':'failed', 'reason': 'Additional Param Supplied.'})
    
    return convertToJson(lawyer.createPaymentRequest(**res))

@api.route('/lawyer/getAccountDetails', methods=['POST'])
def lawyer_getAccountDetails():
    res = dataSource(request)
    params = inspect.getargspec(lawyer.getAccountDetails).args

    # check params should be in res
    if (not validateResponse(params, res)):
        return jsonify({'res': 'failed', 'type':'missing params %s' %returnMissingParams(params, res)})
    
    if(not addtionalParams(params, res)):
        return jsonify({'res':'failed', 'reason': 'Additional Param Supplied.'})
    
    return convertToJson(lawyer.getAccountDetails(**res))