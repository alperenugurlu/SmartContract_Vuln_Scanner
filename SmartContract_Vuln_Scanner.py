import requests

def check_contract_vulnerabilities():
    api_key = input("Etherscan API anahtarınızı girin: ")
    contract_address = input("Akıllı sözleşme adresini girin: ")

    # Etherscan API'sine istek gönderme
    url = f'https://api.etherscan.io/api?module=contract&action=getsourcecode&address={contract_address}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()

    if data['status'] == '1':
        source_code = data['result'][0]['SourceCode']

        # Zafiyet analizi yapmak için gerekli kontrolleri burada yapabilirsiniz
        vulnerabilities = []

        # Örnek Kontroller:
        if 'selfdestruct' in source_code:
            vulnerabilities.append('selfdestruct kullanılmış')
        if 'tx.origin' in source_code:
            vulnerabilities.append('tx.origin kullanılmış')
        if 'delegatecall' in source_code:
            vulnerabilities.append('delegatecall kullanılmış')
        if 'reentrancy' in source_code:
            vulnerabilities.append('reentrancy zafiyeti tespit edildi')
        if 'block.timestamp' in source_code:
            vulnerabilities.append('block.timestamp kullanılmış')
        if 'gasleft()' in source_code:
            vulnerabilities.append('gasleft() kullanılmış')
        if 'assert' in source_code:
            vulnerabilities.append('assert kullanılmış')
        if 'throw' in source_code:
            vulnerabilities.append('throw kullanılmış')
        if 'low-level calls' in source_code:
            vulnerabilities.append('low-level çağrılar kullanılmış')    
        if 'unchecked-send' in source_code:
            vulnerabilities.append('unchecked-send kullanılmış')
        if 'integer overflow' in source_code:
            vulnerabilities.append('integer overflow zafiyeti tespit edildi')
        if 'integer underflow' in source_code:
            vulnerabilities.append('integer underflow zafiyeti tespit edildi')
        if 'timestamp dependence' in source_code:
            vulnerabilities.append('timestamp dependence zafiyeti tespit edildi')
        if 'randomness generation' in source_code:
            vulnerabilities.append('randomness generation zafiyeti tespit edildi')
        if 'unprotected functions' in source_code:
            vulnerabilities.append('unprotected functions tespit edildi')
        if 'DoS (Denial of Service)' in source_code:
            vulnerabilities.append('DoS (Denial of Service) zafiyeti tespit edildi')
        if 'function visibility' in source_code:
            vulnerabilities.append('function visibility zafiyeti tespit edildi')
        if 'repeated-nonce reuse' in source_code:
            vulnerabilities.append('repeated-nonce reuse zafiyeti tespit edildi')
        if 'unchecked-call-return' in source_code:
            vulnerabilities.append('unchecked-call-return kullanılmış')
        if 'missing input validation' in source_code:
            vulnerabilities.append('missing input validation tespit edildi')
        if 'arbitrary contract storage modification' in source_code:
            vulnerabilities.append('arbitrary contract storage modification zafiyeti tespit edildi')

        # Zafiyetleri raporlama
        if vulnerabilities:
            print(f'Akıllı sözleşme zafiyetleri: {", ".join(vulnerabilities)}')
        else:
            print('Akıllı sözleşme güvenli.')

    else:
        print('Hata: Akıllı sözleşme bilgileri alınamadı.')

check_contract_vulnerabilities()

