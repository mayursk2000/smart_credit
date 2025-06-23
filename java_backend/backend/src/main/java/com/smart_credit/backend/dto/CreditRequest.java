package com.smart_credit.backend.dto;

import lombok.Data;
import java.util.Map;

@Data
public class CreditRequest {
    private Map<String, Double> features;
}
