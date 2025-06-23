package com.smart_credit.backend.service;

import com.smart_credit.backend.dto.*;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
@RequiredArgsConstructor
public class MLservice {
    private final RestTemplate restTemplate = new RestTemplate();

    @Value("${ml.api.url}")
    private String mlApiUrl;

    public CreditResponse getPrediction(CreditRequest request){
        return restTemplate.postForObject(mlApiUrl, request.getFeatures(), CreditResponse.class);
    }
}
