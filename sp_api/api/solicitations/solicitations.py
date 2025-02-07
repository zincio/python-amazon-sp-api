from __future__ import absolute_import
import urllib2, urllib, urlparse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class Solicitations(Client):
    u"""
    Solicitations SP-API Client
    :link: 

    With the Solicitations API you can build applications that send non-critical solicitations to buyers. You can get a list of solicitation types that are available for an order that you specify, then call an operation that sends a solicitation to the buyer for that order. Buyers cannot respond to solicitations sent by this API, and these solicitations do not appear in the Messaging section of Seller Central or in the recipient's Message Center. The Solicitations API returns responses that are formed according to the <a href=https://tools.ietf.org/html/draft-kelly-json-hal-08>JSON Hypertext Application Language</a> (HAL) standard.
    """


    @sp_endpoint(u'/solicitations/v1/orders/{}', method=u'GET')
    def get_solicitation_actions_for_order(self, amazonOrderId, **kwargs):
        u"""
        get_solicitation_actions_for_order(self, amazonOrderId, **kwargs) -> ApiResponse

        Returns a list of solicitation types that are available for an order that you specify. A solicitation type is represented by an actions object, which contains a path and query parameter(s). You can use the path and parameter(s) to call an operation that sends a solicitation. Currently only the productReviewAndSellerFeedbackSolicitation solicitation type is available.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            amazonOrderId:string | * REQUIRED An Amazon order identifier. This specifies the order for which you want a list of available solicitation types.
            key marketplaceIds:array | * REQUIRED A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.

        Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop(u'path'), amazonOrderId), params=kwargs)

    @sp_endpoint(u'/solicitations/v1/orders/{}/solicitations/productReviewAndSellerFeedback', method=u'POST')
    def create_product_review_and_seller_feedback_solicitation(self, amazonOrderId, **kwargs):
        u"""
        create_product_review_and_seller_feedback_solicitation(self, amazonOrderId, **kwargs) -> ApiResponse

        Sends a solicitation to a buyer asking for seller feedback and a product review for the specified order. Send only one productReviewAndSellerFeedback or free form proactive message per order.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            amazonOrderId:string | * REQUIRED An Amazon order identifier. This specifies the order for which a solicitation is sent.
            key marketplaceIds:array | * REQUIRED A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.

        Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop(u'path'), amazonOrderId), params=kwargs)
    
