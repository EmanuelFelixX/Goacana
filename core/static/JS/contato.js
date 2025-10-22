function enviarWhats(){
    event.preventDefault();
    const nome = document.getElementById('nome').value;
    const assunto = document.getElementById('assunto').value;
    const telefone = '558491061685';
    const mensagem = `Olá, meu nome é ${nome}. Gostaria de falar sobre ${assunto}.`;
    const msgFormatada = encodeURIComponent(mensagem);
    const url = `https://wa.me/${telefone}?text=${msgFormatada}`;
    window.open(url, '_blank');

}
