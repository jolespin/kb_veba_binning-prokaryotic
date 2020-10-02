# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except ImportError:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class KBParallel(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://ci.kbase.us/services/auth/api/legacy/KBase/Sessions/Login',
            service_ver='release',
            async_job_check_time_ms=100, async_job_check_time_scale_percent=150, 
            async_job_check_max_time_ms=300000):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = service_ver
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc,
            async_job_check_time_ms=async_job_check_time_ms,
            async_job_check_time_scale_percent=async_job_check_time_scale_percent,
            async_job_check_max_time_ms=async_job_check_max_time_ms)

    def run_batch(self, params, context=None):
        """
        :param params: instance of type "RunBatchParams" (runner =
           serial_local | parallel_local | parallel serial_local will run
           tasks on the node in serial, ignoring the concurrent task limits
           parallel_local will run multiple tasks on the node in parallel,
           and will ignore the njsw_task parameter. Unless you know where
           your job will run, you probably don't want to set this higher than
           2 parallel will look at both the local task and njsw task limits
           and operate appropriately. Therefore, you could always just select
           this option and tweak the task limits to get either serial_local
           or parallel_local behavior. TODO: wsid - if defined, the workspace
           id or name (service will handle either string or int) on which to
           attach the job. Anyone with permissions to that WS will be able to
           view job status for this run.) -> structure: parameter "tasks" of
           list of type "Task" (Specifies a task to run.  Parameters is an
           arbitrary data object passed to the function.  If it is a list,
           the params will be interpreted as) -> structure: parameter
           "function" of type "Function" (Specifies a specific KBase module
           function to run) -> structure: parameter "module_name" of String,
           parameter "function_name" of String, parameter "version" of
           String, parameter "params" of unspecified object, parameter
           "runner" of String, parameter "concurrent_local_tasks" of Long,
           parameter "concurrent_njsw_tasks" of Long, parameter "max_retries"
           of Long
        :returns: instance of type "BatchResults" (The list of results will
           be in the same order as the input list of tasks.) -> structure:
           parameter "results" of list of type "TaskResult" -> structure:
           parameter "is_error" of type "boolean" (A boolean - 0 for false, 1
           for true. @range (0, 1)), parameter "result_package" of type
           "ResultPackage" -> structure: parameter "function" of type
           "Function" (Specifies a specific KBase module function to run) ->
           structure: parameter "module_name" of String, parameter
           "function_name" of String, parameter "version" of String,
           parameter "result" of unspecified object, parameter "error" of
           unspecified object, parameter "run_context" of type "RunContext"
           (location = local | njsw job_id = '' | [njsw_job_id] May want to
           add: AWE node ID, client group, total run time, etc) -> structure:
           parameter "location" of String, parameter "job_id" of String
        """
        return self._client.run_job('KBParallel.run_batch',
                                    [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.run_job('KBParallel.status',
                                    [], self._service_ver, context)
